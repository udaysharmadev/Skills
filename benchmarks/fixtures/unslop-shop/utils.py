"""Shared formatting helpers."""
import os


def format_price(cents):
    return f"${cents / 100:.2f}"
