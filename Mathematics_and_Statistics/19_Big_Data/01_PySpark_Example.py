import kagglehub  # For downloading the dataset.
from pyspark.sql import SparkSession  # For creating a SparkSession.
from pyspark.sql.functions import col, when, lower, regexp_replace, count  # Used for data cleaning and transformation.
from pyspark.ml.feature import Tokenizer, StopWordsRemover, CountVectorizer, IDF  #Modules for text processing.
from pyspark.ml.classification import LogisticRegression  # Module for Logistic Regression.
from pyspark.ml import Pipeline  # Automates machine learning workflows.
from pyspark.ml.evaluation import MulticlassClassificationEvaluator as mcce  # Evaluates classification models.


# Step 1: Download the Dataset
path = kagglehub.dataset_download("gracebrasselle/amazon-food-reviews-cleaned")
print("Path to dataset files:", path)

# Step 2: Initialize Spark Session
spark = SparkSession.builder \
    .appName("Amazon Food Reviews Analysis") \
    .getOrCreate()
"""Enables efficient handling of large datasets using Spark's parallel processing capabilities."""

# Step 3: Load the Dataset
# Assuming the dataset has been saved as a CSV file in the downloaded path
file_path = f"{path}/Cleaned_Reviews.csv"
reviews_df = spark.read.csv(file_path, header=True, inferSchema=True)
""" header=True: Uses the first row as column names.
inferSchema=True: Automatically detects data types."""

# Step 4: Explore the Dataset
reviews_df.printSchema()
reviews_df.show(5)
""" Displays the schema and first few rows of the dataset."""

# Step 5: Data Cleaning and Transformation
# Select relevant columns and clean the text data
cleaned_df = reviews_df.select(
    col("Text").alias("review_text"),
    col("Score").alias("rating")
).dropna()
""" Reduces unnecessary data, focusing only on essential columns for analysis."""

# Map scores to sentiments (1-2: Negative, 4-5: Positive, 3: Neutral)
cleaned_df = cleaned_df.withColumn(
    "sentiment",
    when(col("rating") <= 2, 0).when(col("rating") >= 4, 1).otherwise(2)
)
""" Converts numerical ratings to sentiment categories: Negative (0), Positive (1), Neutral (2)."""

# Remove unnecessary characters from the text
cleaned_df = cleaned_df.withColumn(
    "cleaned_review",
    lower(regexp_replace(col("review_text"), "[^a-zA-Z\\s]", ""))
)
""" Converts text to lowercase and removes non-alphanumeric characters."""

cleaned_df.show(5)

# Step 6: Feature Engineering for ML
# Tokenize, remove stop words, and apply TF-IDF
tokenizer = Tokenizer(inputCol="cleaned_review", outputCol="words")
stopwords_remover = StopWordsRemover(inputCol="words", outputCol="filtered_words")
vectorizer = CountVectorizer(inputCol="filtered_words", outputCol="raw_features")
idf = IDF(inputCol="raw_features", outputCol="features")
""" Tokenizer: Splits text into words.
StopWordsRemover: Removes common, irrelevant words.
CountVectorizer: Converts text into a bag-of-words representation.
IDF: Transforms bag-of-words into a weighted representation.
Converts raw text into numerical features suitable for ML algorithms."""

# Step 7: Build a Simple Logistic Regression Model
lr = LogisticRegression(featuresCol="features", labelCol="sentiment")
""" Provides a simple and effective classification method for text data."""

# Create a Pipeline
pipeline = Pipeline(stages=[tokenizer, stopwords_remover, vectorizer, idf, lr])
""" Combines all preprocessing steps and the model into a single workflow.
Simplifies model training and ensures consistency across datasets."""

# Step 8: Split the Data
train_data, test_data = cleaned_df.randomSplit([0.8, 0.2], seed=42)

# Step 9: Train the Model
model = pipeline.fit(train_data)

# Step 10: Evaluate the Model
predictions = model.transform(test_data)

# Show some predictions
predictions.select("cleaned_review", "sentiment", "prediction").show(5)

# Evaluate using MulticlassClassificationEvaluator
evaluator = mcce(
    labelCol="sentiment", predictionCol="prediction", metricName="accuracy"
)
accuracy = evaluator.evaluate(predictions)
print(f"Model Accuracy: {accuracy:.2f}")
""" Measures how well the model performs on test data."""

# Step 11: Analytics and Insights
# Count positive, negative, and neutral sentiments
sentiment_counts = cleaned_df.groupBy("sentiment").agg(count("*").alias("count"))
sentiment_counts.show()

# Step 12: Stop the Spark Session
spark.stop()
""" Releases resources and ensures clean termination."""