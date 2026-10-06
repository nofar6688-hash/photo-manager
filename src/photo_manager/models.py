from dataclasses import dataclass, field


@dataclass
class PhotoAnalysis:
    filename: str
    resolution: tuple[int, int]
    blur_score: float
    is_duplicate: bool
    duplicate_of: str | None
    quality_score: float
    recommendations: str
    reasons: list[str] = field(default_factory=list)