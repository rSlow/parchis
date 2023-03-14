import {createContext, useState} from "react";

export const ErrorContext = createContext(null)

export function ErrorProvider({children, ...props}) {
    const [errors, setErrors] = useState([])

    function addError(message) {
        setErrors([...errors, message])
    }

    return <ErrorContext.Provider value={{errors, addError}}>
        {children}
    </ErrorContext.Provider>
}