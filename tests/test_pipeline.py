import unittest

from pipeline import pipeline

def test_pipeline_status_valid():
    output = pipeline.getPipelineStatus("Staging")
    assert output is not None

def test_pipeline_status_invalid():
    output = pipeline.getPipelineStatus("Invalid")
    assert output is None

def test_pipeline_status_valid_2():
    output = pipeline.getPipelineStatus("Production")
    assert output is not None

def test_pipeline_status_valid_3():
    output = pipeline.getPipelineStatus("Test")
    assert output is not None

def test_db_connect():
    output = pipeline.connectDB()
    print(output)
    assert output is not None
