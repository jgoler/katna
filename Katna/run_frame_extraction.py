import sys
from frame_extractor import FrameExtractor
print("Python executable path:", sys.executable)


def main(videopath):
    extractor = FrameExtractor()
    frame_indices = extractor.extract_candidate_frame_indices(videopath)
    print("Candidate Key Frame Indices:", frame_indices)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_frame_extraction.py <videopath>")
        sys.exit(1)
    videopath = sys.argv[1]
    main(videopath)
