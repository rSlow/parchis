import React, {useContext, useEffect} from 'react';
import classes from "./Chat.module.css";
import {UserContext} from "../../context/userContext";

const Chat = () => {
    const {user} = useContext(UserContext)

    useEffect(() => {
        
    }, [user])

    return (
        <div className={classes.chat_wrapper}>
            <div className={classes.chat}>
                <ul>
                    <li>123</li>
                    <li>456</li>
                    <li>789</li>
                </ul>
            </div>
        </div>
    );
};

export default Chat;