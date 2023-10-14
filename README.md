# SVG to JSX Converter

## Description
This project includes a GUI application that allows users to convert multiple SVG files into JSX components for use in React applications. The SVG elements are cleaned and optimized during the conversion process.

## Installation
Clone this repository to your local machine and navigate to the project directory. Run the application from the command line or execute the main script using a Python environment.

## Usage
1. Open the application and click the "Convert SVGs to JSX" button.
2. Select the SVG files you want to convert.
3. Choose a location to save the resulting JSX file.
4. The application will show the progress of the conversion, and the JSX file will be saved in the chosen location.

## Example of Generated JSX
```jsx
import React from 'react';

export const ChatIcon = () => (
  <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"><path d="M200-80q-33 0-56.5-23.5T120-160v-560q0-33 23.5-56.5T200-800h40v-80h80v80h320v-80h80v80h40q33 0 56.5 23.5T840-720v560q0 33-23.5 56.5T760-80H200Zm0-80h560v-400H200v400Zm0-480h560v-80H200v80Zm0 0v-80 80Zm280 240q-17 0-28.5-11.5T440-440q0-17 11.5-28.5T480-480q17 0 28.5 11.5T520-440q0 17-11.5 28.5T480-400Zm-160 0q-17 0-28.5-11.5T280-440q0-17 11.5-28.5T320-480q17 0 28.5 11.5T360-440q0 17-11.5 28.5T320-400Zm320 0q-17 0-28.5-11.5T600-440q0-17 11.5-28.5T640-480q17 0 28.5 11.5T680-440q0 17-11.5 28.5T640-400ZM480-240q-17 0-28.5-11.5T440-280q0-17 11.5-28.5T480-320q17 0 28.5 11.5T520-280q0 17-11.5 28.5T480-240Zm-160 0q-17 0-28.5-11.5T280-280q0-17 11.5-28.5T320-320q17 0 28.5 11.5T360-280q0 17-11.5 28.5T320-240Zm320 0q-17 0-28.5-11.5T600-280q0-17 11.5-28.5T640-320q17 0 28.5 11.5T680-280q0 17-11.5 28.5T640-240Z"/></svg>
);

export default ChatIcon;
```

## Contributing
If you want to contribute to this project, feel free to submit pull requests or open issues for any bug reports or feature requests.

## License
This project is licensed under the MIT License.

## Acknowledgements
Thanks to all contributors and users of this application.
