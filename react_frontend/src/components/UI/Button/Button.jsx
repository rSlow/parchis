import React from 'react';

const Button = ({className, children, onClick, ...props}) => {
    const classNames = ["button"]
    if (className) {
        classNames.push(...className.split(" "))
    }

    async function extendedOnClick(e) {
        if (onClick) {
            e.target["classList"].add("is-loading")
            try {
                await onClick()
            } finally {
                e.target["classList"].remove("is-loading")
            }
        }
    }

    return (
        <button className={classNames.join(" ")} onClick={(e) => extendedOnClick(e)} {...props}>
            {children}
        </button>
    );
};
export default Button;