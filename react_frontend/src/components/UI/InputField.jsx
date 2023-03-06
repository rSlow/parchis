import React from 'react';

const InputField = ({type, value, setValue, label, placeholder}) => {
    return (
        <div className="field">
            {label ? <label className="label">{label}</label> : null}
            <div className="control">
                <input
                    className="input"
                    type={type}
                    value={value}
                    onChange={(e) => setValue(e.target.value)}
                    placeholder={placeholder}
                />
            </div>
        </div>
    );
};

export default InputField;