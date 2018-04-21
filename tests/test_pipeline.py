import unittest

from pipeline import pipeline

def test_pipeline_status_valid():
    output = pipeline.getPipelineStatus("Staging")
    assert output is not None

def test_pipeline_status_invalid():
    output = pipeline.getPipelineStatus("Invalid")
    assert output is None
