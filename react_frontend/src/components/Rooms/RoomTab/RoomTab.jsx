import React from 'react';
import classes from "./RoomTab.module.css";

const RoomTab = ({id, is_started, players}) => {
    return (
        <div className={classes.room_tab}>
            id={id},
            is_started={is_started},
            players={players}
        </div>
    );
};

export default RoomTab;