from typing import Iterator, Literal, overload

from deepcodec.attachments.stream import AttachmentStream
from deepcodec.audio.stream import AudioStream
from deepcodec.data.stream import DataStream
from deepcodec.stream import Stream
from deepcodec.subtitles.stream import SubtitleStream
from deepcodec.video.stream import VideoStream

class StreamContainer:
    video: tuple[VideoStream, ...]
    audio: tuple[AudioStream, ...]
    subtitles: tuple[SubtitleStream, ...]
    attachments: tuple[AttachmentStream, ...]
    data: tuple[DataStream, ...]
    other: tuple[Stream, ...]

    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Stream]: ...
    @overload
    def __getitem__(self, index: int) -> Stream: ...
    @overload
    def __getitem__(self, index: slice) -> list[Stream]: ...
    @overload
    def __getitem__(self, index: int | slice) -> Stream | list[Stream]: ...
    def get(
        self,
        *args: int | Stream | dict[str, int | tuple[int, ...]],
        **kwargs: int | tuple[int, ...],
    ) -> list[Stream]: ...
    def best(
        self,
        type: Literal["video", "audio", "subtitle", "data", "attachment"],
        /,
        related: Stream | None = None,
    ) -> Stream | None: ...
