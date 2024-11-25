import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class PortfolioOptimizer:
    def __init__(self, tickers, start_date, end_date, min_position=0.05, max_position=0.40):
        """
        Initialize portfolio optimizer with position size constraints

        Parameters:
        - tickers: list of stock tickers
        - start_date: start date for historical data
        - end_date: end date for historical data
        - min_position: minimum weight for any single position (default 5%)
        - max_position: maximum weight for any single position (default 40%)
        """
        self.tickers = tickers
        self.min_position = min_position
        self.max_position = max_position
        self.data = self._get_stock_data(start_date, end_date)
        self.returns = self.data.pct_change().dropna()
        self.num_assets = len(tickers)

    def _get_stock_data(self, start_date, end_date):
        """Fetch stock data from Yahoo Finance"""
        data = pd.DataFrame()
        for ticker in self.tickers:
            stock_data = yf.download(ticker, start=start_date, end=end_date)['Adj Close']
            data[ticker] = stock_data
        return data

    def calculate_portfolio_metrics(self, weights, returns=None):
        """Calculate portfolio metrics (return, volatility, Sharpe ratio)"""
        if returns is None:
            returns = self.returns

        portfolio_return = np.sum(returns.mean() * weights) * 252
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
        sharpe_ratio = portfolio_return / portfolio_volatility
        return portfolio_return, portfolio_volatility, sharpe_ratio

    def negative_sharpe_ratio(self, weights, returns=None, risk_free_rate=0.02):
        """Calculate negative Sharpe ratio (for minimization)"""
        if returns is None:
            returns = self.returns

        portfolio_return, portfolio_volatility, _ = self.calculate_portfolio_metrics(weights, returns)
        return -(portfolio_return - risk_free_rate) / portfolio_volatility

    def optimize_portfolio(self):
        """
        Find the optimal portfolio weights considering position size constraints
        """
        # Constraints
        constraints = [
            {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}  # weights sum to 1
        ]

        # Position size bounds
        bounds = tuple((self.min_position, self.max_position) for _ in range(self.num_assets))

        # Initial guess (equal weights)
        initial_weights = np.array([1 / self.num_assets] * self.num_assets)

        # Optimize!
        result = minimize(
            self.negative_sharpe_ratio,
            initial_weights,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints,
            options={'maxiter': 1000}
        )

        if not result.success:
            print(f"Optimization Warning: {result.message}")

        return result.x

    def plot_efficient_frontier(self, num_portfolios=1000):
        """
        Plot the efficient frontier with random portfolios and the optimal portfolio
        """
        returns_array = []
        volatility_array = []
        sharpe_array = []
        weights_array = []

        # Generate random portfolios within constraints
        for _ in range(num_portfolios):
            weights = np.random.uniform(self.min_position, self.max_position, self.num_assets)
            weights = weights / np.sum(weights)  # Normalize to sum to 1

            # Ensure minimum position size
            while np.any(weights < self.min_position):
                weights = np.random.uniform(self.min_position, self.max_position, self.num_assets)
                weights = weights / np.sum(weights)

            returns_annual, volatility_annual, sharpe = self.calculate_portfolio_metrics(weights)
            returns_array.append(returns_annual)
            volatility_array.append(volatility_annual)
            sharpe_array.append(sharpe)
            weights_array.append(weights)

        # Find optimal portfolio
        optimal_weights = self.optimize_portfolio()
        optimal_return, optimal_volatility, optimal_sharpe = self.calculate_portfolio_metrics(optimal_weights)

        # Plotting
        plt.figure(figsize=(12, 8))

        # Plot random portfolios colored by Sharpe ratio
        sc = plt.scatter(volatility_array, returns_array,
                         c=sharpe_array, cmap='viridis',
                         alpha=0.5, label='Random Portfolios')
        plt.colorbar(sc, label='Sharpe Ratio')

        # Plot optimal portfolio
        plt.scatter(optimal_volatility, optimal_return,
                    color='red', marker='*', s=200,
                    label=f'Optimal Portfolio (Sharpe: {optimal_sharpe:.2f})')

        plt.xlabel('Expected Volatility')
        plt.ylabel('Expected Return')
        plt.title('Efficient Frontier with Position Size Constraints')
        plt.legend()
        plt.grid(True)
        plt.show()

        return optimal_weights, optimal_return, optimal_volatility, optimal_sharpe

    def generate_report(self):
        """Generate a comprehensive portfolio optimization report"""
        optimal_weights, opt_return, opt_vol, opt_sharpe = self.plot_efficient_frontier()

        print("\n=== Portfolio Optimization Report ===")
        print(f"\nPosition Size Constraints:")
        print(f"Minimum Position: {self.min_position * 100:.1f}%")
        print(f"Maximum Position: {self.max_position * 100:.1f}%")

        print("\nOptimal Portfolio Allocation:")
        for ticker, weight in zip(self.tickers, optimal_weights):
            print(f"{ticker}: {weight * 100:.2f}%")

        print(f"\nPortfolio Metrics:")
        print(f"Expected Annual Return: {opt_return * 100:.2f}%")
        print(f"Expected Annual Volatility: {opt_vol * 100:.2f}%")
        print(f"Sharpe Ratio: {opt_sharpe:.4f}")

        # Calculate and display correlation matrix
        print("\nCorrelation Matrix:")
        correlation_matrix = self.returns.corr()
        print(correlation_matrix.round(2))

        return optimal_weights, opt_return, opt_vol, opt_sharpe


# Example usage
if __name__ == "__main__":
    # Define portfolio parameters
    tickers = ['BEL.NS', 'ZOMATO.NS', 'HFCL.NS', 'IFCI.NS']
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365 * 2)  # 2 years of data

    # Initialize optimizer with position constraints
    optimizer = PortfolioOptimizer(
        tickers=tickers,
        start_date=start_date,
        end_date=end_date,
        min_position=0.05,  # 5% minimum position
        max_position=0.40  # 40% maximum position
    )

    # Generate and display report
    optimizer.generate_report()