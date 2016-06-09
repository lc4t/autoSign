import React, {StyleSheet, Dimensions, PixelRatio} from "react-native";
const {width, height, scale} = Dimensions.get("window"),
    vw = width / 100,
    vh = height / 100,
    vmin = Math.min(vw, vh),
    vmax = Math.max(vw, vh);

export default StyleSheet.create({
    "index-body": {
        "backgroundImage": "url(/static/images/index.jpg)",
        "backgroundRepeat": "no-repeat",
        "backgroundSize": "100%"
    },
    "form-body": {
        "backgroundColor": "#666666"
    }
});