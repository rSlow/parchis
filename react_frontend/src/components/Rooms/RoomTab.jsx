import React from 'react';
import classes from "./RoomTab.module.css";

const RoomTab = ({id, is_started, players}) => {
    async function joinGame(room_id) {
        console.log(room_id)
    }

    async function watchGame(room_id) {
        console.log(room_id)
    }

// "box has-background-light is-flex is-justify-content-space-between p-4 m-4"
    return (
        <div className={classes.room_tab}>
            <div className={classes.players_block}>
                Игроки: {players.length}
                <div className={"player"}>
                    {players.map(player =>
                        <div>
                            {player.user_id}
                        </div>
                    )}
                </div>
            </div>
            <div className={classes.buttons_block}>
                {is_started === false
                    ? <button
                        onClick={() => joinGame(id)}
                    >Присоединиться </button>
                    : <button
                        onClick={() => watchGame(id)}
                    > Посмотреть игру </button>
                }
            </div>
        </div>
    );
};

export default RoomTab;