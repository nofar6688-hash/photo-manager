from src.photo_manager.models import PhotoAnalysis

def test_photo_analysis_creation():
    photo = PhotoAnalysis(
        filename="IMG_001.jpg",
        resolution=(4032, 3024),
        blur_score=85.5,
        is_duplicate=False,
        duplicate_of=None,
        quality_score=90.0,
        recommendations="keep",
        reasons=["Good quality"],
    )
    assert photo.filename == "IMG_001.jpg"
    assert photo.resolution == (4032, 3024)
    assert photo.blur_score == 85.5
    assert photo.is_duplicate is False
    assert photo.duplicate_of == None
    assert photo.quality_score == 90.0
    assert photo.recommendations == "keep"
    assert photo.reasons == ["Good quality"]