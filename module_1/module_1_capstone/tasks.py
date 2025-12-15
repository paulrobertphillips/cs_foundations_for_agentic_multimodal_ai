# tasks.py
from typing import Any, Dict

def prepare_dataset(_: Dict[str, Any] | None = None) -> Dict[str, Any]:
    # Conceptually a goal node; returns a "context" dict for downstream tasks.
    return {"dataset_path": "data.csv"}

def load_data(ctx: Dict[str, Any]) -> Dict[str, Any]:
    # Pretend we loaded a dataset
    return {"rows": 100, "columns": 5, "missing_values": 12, **ctx}

def validate_schema(data: Dict[str, Any]) -> Dict[str, Any]:
    # Pretend schema is valid; attach validation result
    return {**data, "schema_valid": True}

def clean_missing(data: Dict[str, Any]) -> Dict[str, Any]:
    # Pretend we cleaned missing values and reduced rows slightly
    cleaned_rows = data["rows"] - 5
    return {**data, "rows": cleaned_rows, "missing_values": 0}

def compute_features(data: Dict[str, Any]) -> Dict[str, Any]:
    # Pretend we computed features
    return {**data, "features": ["f1", "f2", "f3"]}

# Registry mapping task name -> function
TASKS = {
    "prepare_dataset": prepare_dataset,
    "load_data": load_data,
    "validate_schema": validate_schema,
    "clean_missing": clean_missing,
    "compute_features": compute_features,
}
