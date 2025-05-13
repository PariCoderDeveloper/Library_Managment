from dataclasses import dataclass

@dataclass
class GetBookwithIdDTO:
    title : str
    genre : str
    authors_name : list[str]