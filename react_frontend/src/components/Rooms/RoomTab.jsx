import React, {useContext} from 'react';
import classes from "./RoomTab.module.css";
import {UserContext} from "../../context/userContext";
import RoomsAPI from "../../API/Rooms";
import {useNavigate} from "react-router-dom";

const RoomTab = ({id, is_started, players}) => {
    const {user} = useContext(UserContext)
    const navigate = useNavigate()

    async function joinGame(roomId) {
        await RoomsAPI.join(user.id, roomId)
        navigate(`/room/${roomId}`, {state: roomId})
    }

    async function watchGame(room_id) {
        console.log(room_id)
    }

    return (
        <div className={classes.room_tab}>
            ID #{id}
            <div className={classes.players_block}>
                Игроки: {players.length}
                <div className={"player"}>
                    {players.map(player => {
                        const user = player["user"]
                            return <div key={player.id}>
                                #{user["id"]} {user["email"]}
                            </div>
                        }
                    )}
                </div>
            </div>
            <div className={classes.buttons_block}>
                {is_started === false &&
                    <button
                        onClick={() => joinGame(id)}
                    >Присоединиться </button>}
                {is_started === true &&
                    <button
                        onClick={() => watchGame(id)}
                    > Посмотреть игру </button>}
            </div>
        </div>
    );
};

export default RoomTab;