import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineStyleElementHandler
)
from wagtail.core import hooks


@hooks.register("register_rich_text_features")
def register_redtext_feature(features):
    feature_name = "Red"
    type_ = "CENTERTEXT"
    tag = "div"
    control = {
        "type": type_,
        "label": "R",
        "description": "Red Text",
        "style": {
            "color": "red",
        },
    }
    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )
    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {
            "style_map": {
                type_: {
                    "element": tag,
                    "props": {
                        "style": "color:red",
                    }
                }
            }
        }
    }
    features.register_converter_rule("contentstate", feature_name, db_conversion)
    features.default_features.append(feature_name)
