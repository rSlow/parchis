import classes from "./InputField.module.css";
import React, {useState} from "react";

const InputField = ({label, errorFlag, errorMessage, isPassword, ...props}) => {
    const [isHide, setIsHide] = useState(true)

    function toggleHide() {
        if (isHide === true) {
            setIsHide(false)
        } else {
            setIsHide(true)
        }
    }

    return (
        <div className={`field is-relative`}>
            {label && <label className="label">{label}</label>}
            <div className="control">
                <input className={`input  ${errorFlag && "is-danger"}`}
                       type={isPassword && isHide === true
                           ? "password"
                           : "text"
                       }
                       {...props}
                />
                {isPassword === true &&
                    <img className={classes.hide_img}
                         src={isHide
                             ? require("./eye_closed.png")
                             : require("./eye.png")
                         }
                         alt="hide"
                         onClick={toggleHide}
                    />}
            </div>
            {errorFlag === true &&
                <p className="help mb-3 has-text-danger is-size-6">
                    {errorMessage}
                </p>}
        </div>
    );
};

export default InputField;