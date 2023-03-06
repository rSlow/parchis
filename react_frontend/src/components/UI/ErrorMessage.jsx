import React from 'react';

const ErrorMessage = ({message}) => {
    return (
        <div className="has-text-weight-bold has-text-danger">
            {message}
        </div>
    );
};

export default ErrorMessage;