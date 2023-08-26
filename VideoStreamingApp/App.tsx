/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 */

import React from 'react';
import {SafeAreaView, ScrollView, useColorScheme, View} from 'react-native';

import VideoComponent from './VideoComponent';

function App(): JSX.Element {
  const isDarkMode = useColorScheme() === 'dark';

  return (
    <SafeAreaView>
      <ScrollView contentInsetAdjustmentBehavior="automatic">
        <View
          style={{
            backgroundColor: isDarkMode ? 'black' : 'white',
          }}>
          <VideoComponent />
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

export default App;
