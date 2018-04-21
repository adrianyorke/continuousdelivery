import unittest

from pipeline import pipeline
    
def test_status():
    output = pipeline.getPipelineStatus("Staging")
    assert output is not None
