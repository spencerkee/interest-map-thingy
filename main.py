from loguru import logger
import urllib.request
import streamlit as st
from loguru import logger
import math
from backend.dataset import Dataset
from backend.database import Database
from backend.vectorstore import VectorStore
from configuration import Configuration
import constants
from backend.loader import DocumentLoader
from utils import pretty_print_docs, format_docs
import re
import urllib
import requests
import sys


def main():
    # logger.info("Starting GUI...")
    # gui = GUI()
    # gui.run()
    dataset = Dataset(constants.DATASET_FILE)
    loader = DocumentLoader(Configuration())
    vector_store = VectorStore(loader, Configuration())
    vector_store.init_vectorstore()
    import ipdb

    ipdb.set_trace()
    pass


if __name__ == "__main__":
    main()
