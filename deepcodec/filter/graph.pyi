from fractions import Fraction
from typing import Any

from deepcodec.audio.format import AudioFormat
from deepcodec.audio.frame import AudioFrame
from deepcodec.audio.layout import AudioLayout
from deepcodec.audio.stream import AudioStream
from deepcodec.video.format import VideoFormat
from deepcodec.video.frame import VideoFrame
from deepcodec.video.stream import VideoStream

from .context import FilterContext
from .filter import Filter

class Graph:
    configured: bool

    def __init__(self) -> None: ...
    def configure(self, auto_buffer: bool = True, force: bool = False) -> None: ...
    def link_nodes(self, *nodes: FilterContext) -> Graph: ...
    def add(
        self, filter: str | Filter, args: Any = None, **kwargs: str
    ) -> FilterContext: ...
    def add_buffer(
        self,
        template: VideoStream | None = None,
        width: int | None = None,
        height: int | None = None,
        format: VideoFormat | None = None,
        name: str | None = None,
        time_base: Fraction | None = None,
    ) -> FilterContext: ...
    def add_abuffer(
        self,
        template: AudioStream | None = None,
        sample_rate: int | None = None,
        format: AudioFormat | str | None = None,
        layout: AudioLayout | str | None = None,
        channels: int | None = None,
        name: str | None = None,
        time_base: Fraction | None = None,
    ) -> FilterContext: ...
    def set_audio_frame_size(self, frame_size: int) -> None: ...
    def push(self, frame: None | AudioFrame | VideoFrame) -> None: ...
    def pull(self) -> VideoFrame | AudioFrame: ...
    def vpush(self, frame: VideoFrame | None) -> None: ...
    def vpull(self) -> VideoFrame: ...
