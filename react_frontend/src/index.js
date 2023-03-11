import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bulma/css/bulma.css'
import App from './App';

import {UserProvider} from "./context/userContext";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
        // <UserProvider>
            <App/>
        // </UserProvider>
);
