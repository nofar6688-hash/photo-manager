from src.photo_manager.blur_detector import calculate_blur_score
from src.photo_manager.blur_detector import (
    calculate_regional_blur_scores,
)

def test_blur_score_returns_positive_number():
    score = calculate_blur_score("samples/IMG_test.jpeg")

    assert isinstance(score, float)
    assert score > 0

def test_regional_blur_returns_nine_scores():
    scores = calculate_regional_blur_scores("samples/IMG_test.jpeg")

    assert len(scores) == 9
    assert all(isinstance(score, float) for score in scores)

def test_regional_blur_supports_custom_grid_size():
    scores = calculate_regional_blur_scores("samples/IMG_test.jpeg", grid_size=2,)

    assert len(scores) == 4
