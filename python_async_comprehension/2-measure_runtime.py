#!/usr/bin/env python3
"""
Module for pagination of popular baby names data.
"""


import csv
from typing import List, Dict
import os


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = os.path.join(
        os.path.dirname(__file__), "Popular_Baby_Names.csv"
    )

    def __init__(self):
        """Initializes the server and data variables."""
        self.__dataset = None  # Stores the loaded dataset
        self.__indexed_dataset = None  # Stores the indexed dataset

    def dataset(self) -> List[List]:
        """Loads and returns the dataset, caching it for future access."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Returns a dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()  # Load the dataset if not cached
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a paginated dataset starting from a given index.
        
        Args:
            index (int): The index from which to start pagination.
            page_size (int): The number of items to return on the page.

        Returns:
            Dict: A dictionary containing the starting index, paginated data,
                  page size, and the next index for pagination.
        """
        assert index is not None and index >= 0, "index must be positive"

        indexed_dataset = self.indexed_dataset()
        assert index < len(indexed_dataset), "no access"

        data = []
        current_index = index
        for _ in range(page_size):
            # Find the next valid index in the indexed dataset
            while current_index not in indexed_dataset:
                current_index += 1
                if current_index >= len(indexed_dataset):
                    break
            if current_index >= len(indexed_dataset):
                break
            data.append(indexed_dataset[current_index])  # Add the data to the page
            current_index += 1

        next_index = current_index  # Index for the next page
        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": next_index,
        }
