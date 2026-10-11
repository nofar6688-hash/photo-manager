import cv2

def calculate_blur_score(image_path: str) -> float:
    """
    Calculate the blur score of an image using the variance of the Laplacian method.

    Args:
        image_path (str): The path to the image file.

    Returns:
        float: The calculated blur score. Higher values indicate a sharper image.
    """
    # Read the image from the specified path
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute the Laplacian of the grayscale image
    score = cv2.Laplacian(grayscale, cv2.CV_64F).var()

    return float(score)


def calculate_regional_blur_scores(
        image_path: str,
        grid_size: int = 3,
) -> list[float]:
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    if grid_size < 1:
        raise ValueError("Grid size must be at least 1")

    height, width = image.shape[:2]
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    scores = []

    for row in range(grid_size):
        for col in range(grid_size):
            # Calculate the coordinates of the current grid cell
            x_start = col * width // grid_size
            x_end = (col + 1) * width // grid_size
            y_start = row * height // grid_size
            y_end = (row + 1) * height // grid_size

            # Extract the region of interest (ROI)
            region = grayscale[y_start:y_end, x_start:x_end]

            # Compute the Laplacian of the ROI and calculate its variance
            score = cv2.Laplacian(region, cv2.CV_64F).var()
            scores.append(float(score))

    return scores