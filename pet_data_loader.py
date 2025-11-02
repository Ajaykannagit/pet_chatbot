# pet_data_loader.py - Download and manage pet data
import requests
import json
import os
from config import DATA_SOURCES, FALLBACK_DATA

class PetDataLoader:
    def __init__(self):
        self.data_dir = "data"
        self.create_data_directory()
        self.loaded_data = {}
        
    def create_data_directory(self):
        """Create data folder if it doesn't exist"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            print("[info] Created data directory")
    
    def download_pet_data(self, data_type):
        """Download pet data from online sources"""
        if data_type in DATA_SOURCES:
            try:
                print(f"[info] Attempting to download {data_type} data...")
                response = requests.get(DATA_SOURCES[data_type], timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Process the data based on API response format
                    processed_data = self.process_api_data(data_type, data)
                    
                    # Save to local file
                    filename = os.path.join(self.data_dir, f"{data_type}.json")
                    with open(filename, 'w') as f:
                        json.dump(processed_data, f, indent=2)
                    
                    self.loaded_data[data_type] = processed_data
                    print(f"[ok] {data_type} data downloaded successfully!")
                    return processed_data
                else:
                    print(f"[error] Failed to download {data_type} data (Status: {response.status_code})")
                    
            except Exception as e:
                print(f"[error] Error downloading {data_type}: {e}")
        
        # If download fails, use fallback data
        print(f"[fallback] Using fallback data for {data_type}")
        if data_type in FALLBACK_DATA:
            self.loaded_data[data_type] = FALLBACK_DATA[data_type]
            return FALLBACK_DATA[data_type]
        
        return None
    
    def process_api_data(self, data_type, raw_data):
        """Process raw API data into our expected format"""
        if data_type == "dogs":
            # Dog API returns breed list, we'll use fallback for advice
            return FALLBACK_DATA["dogs"]
        elif data_type == "cats":
            # Cat API returns breed info, we'll use fallback for advice
            return FALLBACK_DATA["cats"]
        else:
            return raw_data
    
    def load_data(self, data_type):
        """Load data from local file or download if not exists"""
        filename = os.path.join(self.data_dir, f"{data_type}.json")
        
        # Try to load from local file first
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    self.loaded_data[data_type] = json.load(f)
                print(f"[ok] Loaded {data_type} data from local file")
                return self.loaded_data[data_type]
            except Exception as e:
                print(f"[error] Error loading local {data_type} data: {e}")
        
        # If local file doesn't exist or is corrupt, download or use fallback
        return self.download_pet_data(data_type)
    
    def get_pet_advice(self, animal_type, problem):
        """Get advice for specific animal and problem"""
        # Try to get from loaded data first
        if animal_type in self.loaded_data:
            animal_data = self.loaded_data[animal_type]
            if problem in animal_data:
                return animal_data[problem]
        
        # Fallback to general advice
        if problem in FALLBACK_DATA.get("general", {}):
            return FALLBACK_DATA["general"][problem]
        
        # Ultimate fallback
        return f"I have information about {animal_type} {problem}. For specific advice, consult your veterinarian."
    
    def check_emergency(self, user_input):
        """Check if the user input indicates an emergency"""
        user_input = user_input.lower()
        emergency_keywords = FALLBACK_DATA["emergency"]["keywords"]
        
        for keyword in emergency_keywords:
            if keyword in user_input:
                return FALLBACK_DATA["emergency"]["response"], FALLBACK_DATA["emergency"]["emotion"]
        
        return None, None
    
    def initialize_all_data(self):
        """Download/Load all pet data on startup"""
        print("[init] Initializing pet data...")
        data_types = list(DATA_SOURCES.keys())
        for data_type in data_types:
            self.load_data(data_type)
        print("[ok] Pet data initialization complete!")
        print(f"[stats] Loaded data for: {list(self.loaded_data.keys())}")

# Create global instance
pet_data = PetDataLoader()