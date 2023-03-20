import React from 'react';

const RoomPlayer = ({player}) => {
    async function setPlayerInfo() {

    }

    return (
        <div className="box p-2 mb-1">
            {JSON.stringify(player.user)}
        </div>
    );
};

export default RoomPlayer;