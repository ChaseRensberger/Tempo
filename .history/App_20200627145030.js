import { StatusBar } from 'expo-status-bar';
import React, { useState } from 'react';
import { StyleSheet, Text, View, TextInput } from 'react-native';

const fetchFonts = () => {
  return Font.loadAsync({
    'montserrat': require('./assets/fonts/Montserrat-Regular.ttf'),
    'montserrat-bold': require('./assets/fonts/Montserrat-Bold.ttf')
  });
}

export default function App() {
  const [song, setSong] = useState('');
  return (
    <View style={styles.container}>
      <Text style = {{
                paddingTop: 0,
                paddingBottom: 4,
                fontFamily: 'montserrat',
                fontSize: 16,
                color: '#5A6067',
            }}>Enter Your Song Here!</Text>
        
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
