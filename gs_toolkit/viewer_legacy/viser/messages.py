"""Message type definitions. For synchronization with the TypeScript definitions, see
`_typescript_interface_gen.py.`"""

from __future__ import annotations

import dataclasses
from typing import Any, Literal, Optional, Tuple

import viser.infra
from typing_extensions import override


class GSTKMessage(viser.infra.Message):
    """Base message type for controlling our viewer."""

    @override
    def redundancy_key(self) -> str:
        return type(self).__name__


@dataclasses.dataclass
class BackgroundImageMessage(GSTKMessage):
    """Message for rendering a background image."""

    media_type: Literal["image/jpeg", "image/png"]
    base64_data: str


@dataclasses.dataclass
class GuiAddMessage(GSTKMessage):
    """Sent server->client to add a new GUI input."""

    name: str
    folder_labels: Tuple[str, ...]
    leva_conf: Any

    @override
    def redundancy_key(self) -> str:
        return f"{type(self).__name__}_{self.name}"


@dataclasses.dataclass
class GuiRemoveMessage(GSTKMessage):
    """Sent server->client to add a new GUI input."""

    name: str

    @override
    def redundancy_key(self) -> str:
        return f"{type(self).__name__}_{self.name}"


@dataclasses.dataclass
class GuiUpdateMessage(GSTKMessage):
    """Sent client->server when a GUI input is changed."""

    name: str
    value: Any

    @override
    def redundancy_key(self) -> str:
        return f"{type(self).__name__}_{self.name}"


@dataclasses.dataclass
class GuiSetHiddenMessage(GSTKMessage):
    """Sent client->server when a GUI input is changed."""

    name: str
    hidden: bool

    @override
    def redundancy_key(self) -> str:
        return f"{type(self).__name__}_{self.name}"


@dataclasses.dataclass
class GuiSetValueMessage(GSTKMessage):
    """Sent server->client to set the value of a particular input."""

    name: str
    value: Any

    @override
    def redundancy_key(self) -> str:
        return f"{type(self).__name__}_{self.name}"


@dataclasses.dataclass
class GuiSetLevaConfMessage(GSTKMessage):
    """Sent server->client to override some part of an input's Leva config."""

    name: str
    leva_conf: Any

    @override
    def redundancy_key(self) -> str:
        return f"{type(self).__name__}_{self.name}"


@dataclasses.dataclass
class FilePathInfoMessage(GSTKMessage):
    """Experiment file path info"""

    config_base_dir: str
    """ Base directory for config files """
    data_base_dir: str
    """ Base directory for data files """
    export_path_name: str
    """ Name of the export folder """


@dataclasses.dataclass
class SetCameraMessage(GSTKMessage):
    """Set the current camera."""

    fov: Optional[float]
    """ Field of view of the camera """
    look_at: Optional[Tuple[float, float, float]]
    """Point in 3D the camera is looking at"""
    position: Optional[Tuple[float, float, float]]
    """ Position of the camera"""
    instant: bool = False
    """ Whether to move the camera instantly or animate it"""


@dataclasses.dataclass
class CameraMessage(GSTKMessage):
    """Render camera data."""

    aspect: float
    """ Aspect ratio of the camera """
    render_aspect: float
    """ Aspect ratio of the render window """
    fov: float
    """ Field of view of the camera """
    matrix: Tuple[
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
        float,
    ]
    """ Camera matrix """
    camera_type: Literal["perspective", "fisheye", "equirectangular"]
    """ Camera type """
    is_moving: bool
    """ True if the camera is moving, False otherwise """
    timestamp: int
    """JSON computed by the camera class"""


@dataclasses.dataclass
class SceneBoxMessage(GSTKMessage):
    """Scene Box data."""

    min: Tuple[float, float, float]
    """ Minimum coordinates of the scene box """
    max: Tuple[float, float, float]
    """ Maximum coordinates of the scene box """


@dataclasses.dataclass
class DatasetImageMessage(GSTKMessage):
    """Message for rendering a dataset image frustum."""

    idx: str
    """Index of the image in the threejs scene"""
    json: Any
    """JSON computed by the camera class"""

    @override
    def redundancy_key(self) -> str:
        return f"{type(self).__name__}_{self.idx}"


@dataclasses.dataclass
class TrainingStateMessage(GSTKMessage):
    """Whether the scene is in training mode or not."""

    training_state: Literal["training", "paused", "completed"]
    """True if the model is currently training, False otherwise"""


@dataclasses.dataclass
class CameraPathPayloadMessage(GSTKMessage):
    """Camera path"""

    camera_path_filename: str
    """ Camera path filename """
    camera_path: Any
    """ Camera path data """


@dataclasses.dataclass
class CameraPathOptionsRequest(GSTKMessage):
    """Request list of existing camera paths"""


@dataclasses.dataclass
class CameraPathsMessage(GSTKMessage):
    """Dictionary of camera paths"""

    payload: Any
    """ Dictionary of camera paths """


@dataclasses.dataclass
class CropParamsMessage(GSTKMessage):
    """Crop parameters"""

    crop_enabled: bool
    """ Crop parameters """
    crop_bg_color: Tuple[int, int, int]
    """ Crop background color, range 0-255 """
    crop_center: Tuple[float, float, float]
    """ Center of the crop box """
    crop_scale: Tuple[float, float, float]
    """ Scale of the crop box """


@dataclasses.dataclass
class StatusMessage(GSTKMessage):
    """Status message."""

    eval_res: str
    """ Resolution of the viewer display in plain text """
    step: int
    """ Current step """


@dataclasses.dataclass
class SaveCheckpointMessage(GSTKMessage):
    """Save checkpoint message."""


@dataclasses.dataclass
class UseTimeConditioningMessage(GSTKMessage):
    """Use time conditioning message."""


@dataclasses.dataclass
class TimeConditionMessage(GSTKMessage):
    """Time conditioning message."""

    time: float
    """ Time conditioning value """


@dataclasses.dataclass
class ClickMessage(GSTKMessage):
    """Click message."""

    origin: Tuple[float, float, float]
    """The origin of the click in world coords (center of camera)"""
    direction: Tuple[float, float, float]
    """The direction of the click if projected through the clicked pixel (world coords)"""


@dataclasses.dataclass
class OutputOptionsMessage(GSTKMessage):
    """Output options message which are used in the export panel.
    TODO: remove when export panel is becomes python defined.
    """

    options: Any
    """ List of output option strings"""
