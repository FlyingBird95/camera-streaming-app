import React from 'react';
import {StyleSheet, Text} from 'react-native';
// @ts-ignore
import Video from 'react-native-video';

interface VideoComponentProps {
  uri: string;
}

interface VideoComponentState {
  error: string;
}

class VideoComponent extends React.Component<
  VideoComponentProps,
  VideoComponentState
> {
  constructor(props: VideoComponentProps) {
    super(props);
    this.state = {error: ''};
  }
  onError = async (error: string) => {
    console.log(error);
    this.setState({error: JSON.stringify(error)});
  };
  render() {
    if (this.state.error) {
      return <Text>{this.state.error}</Text>;
    }

    return (
      <Video
        source={{uri: 'https://cdn.flowplayer.com/a30bd6bc-f98b-47bc-abf5-97633d4faea0/hls/de3f6ca7-2db3-4689-8160-0f574a5996ad/playlist.m3u8'}}
        onError={this.onError}
        paused={false}
        repeat={true}
        style={styles.backgroundVideo}
      />
    );
  }
}
var styles = StyleSheet.create({
  backgroundVideo: {
    position: 'absolute',
    height: '100%',
    width: '100%',
    top: 0,
    left: 0,
    bottom: 0,
    right: 0,
  },
});
export default VideoComponent;
