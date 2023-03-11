import React from 'react';

const RoomTab = ({id, is_started, players}) => {
    return (
        <div className={"room"}>
            id={id},
            is_started={is_started},
            players={players}
        </div>
    );
};

export default RoomTab;