import os
from seamless_interaction.fs import SeamlessInteractionFS
import json
import numpy as np
import cv2
import librosa

class InteractionDataLoader:
    def __init__(self, config=None):
        self.fs = SeamlessInteractionFS(config=config)

    def get_paths(self, file_id):
        """Return all local file paths for a given file ID."""
        return self.fs.get_path_list_for_file_id_local(file_id)

    def load_interaction(self, file_id):
        """Load all modalities for a given file ID."""
        paths = self.get_paths(file_id)
        data = {}
        for path in paths:
            if path.endswith('.mp4'):
                data['video'] = cv2.VideoCapture(path)
            elif path.endswith('.wav'):
                audio, sr = librosa.load(path, sr=None)
                data['audio'] = {'array': audio, 'sampling_rate': sr}
            elif path.endswith('.json'):
                with open(path, 'r') as f:
                    data['json'] = json.load(f)
            elif path.endswith('.npz'):
                data['npz'] = np.load(path, allow_pickle=True)
        return data

    def sample_random_file_ids(self, num_samples=1):
        """Sample random file IDs from the dataset."""
        return self.fs.sample_random_file_ids(num_samples=num_samples)

# Example usage
if __name__ == "__main__":
    import glob
    # Path to session groups
    base_dir = "/Users/bloggerwang/Documents/Lab/seamless_interaction/analysis/dataset/session_groups/improvised/dev/0000/"
    loader = InteractionDataLoader()
    # Find all .json files in all subfolders
    json_files = glob.glob(os.path.join(base_dir, "*/", "*.json"))
    file_ids = [os.path.splitext(os.path.basename(f))[0] for f in json_files]
    print(f"Found {len(file_ids)} file IDs in session groups.")
    for file_id in file_ids:
        print(f"\nLoading {file_id}...")
        interaction = loader.load_interaction(file_id)
        print(f"Available keys: {list(interaction.keys())}")
        if 'npz' in interaction:
            print(f"NPZ keys: {list(interaction['npz'].keys())}")
            if 'smplh:right_hand_pose' in interaction['npz']:
                print(f"Right hand pose shape: {interaction['npz']['smplh:right_hand_pose'].shape}")
