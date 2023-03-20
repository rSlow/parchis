import React, {useContext} from 'react';
import classes from "./RoomTab.module.css";
import {useNavigate} from "react-router-dom";
import {UserContext} from "../../../context/userContext";
import RoomsAPI from "../../../API/Rooms";
import Button from "../../UI/Button/Button";
import {loginAPI} from "../../../API/Login";

const RoomTab = ({room}) => {

    const {user, isAuth} = useContext(UserContext)
    const navigate = useNavigate()
    const players = room["players"]

    async function joinGame(roomId) {
        await RoomsAPI.joinRoom(user.id, roomId)
        navigate(`/room/${roomId}`, {state: roomId})
    }

    async function returnToGame(roomId) {
        navigate(`/room/${roomId}`, {state: roomId})
    }

    async function watchGame(room_id) {
        console.log(room_id)
    }

    return (
        <div className={classes.room_tab}>
            <h1 className={classes.room_name}>{room.name}</h1>

            <div className={classes.players_block}>
                Игроки: {players.length}
                <div className={"player"}>
                    {players.map(player => {
                            const user = player.user
                            return <div key={user?.id}>
                                #{user?.id} {user?.username}
                            </div>
                        }
                    )}
                </div>
            </div>
            <div className={classes.buttons_block}>

                {isAuth && room["is_started"] === false && room["is_joinable"] === true &&
                    <Button className="button is-link is-small is-outlined"
                            onClick={() => joinGame(room.id)}
                    >Присоединиться </Button>}

                {isAuth && room["is_current"] === true &&
                    <Button className="button is-danger is-small is-outlined"
                            onClick={() => returnToGame(room.id)}
                    > Вернуться </Button>}

                {room["is_started"] === true && room["is_current"] === false &&
                    <Button className="is-success is-small mx-1"
                            onClick={() => watchGame(room.id)}
                    > Посмотреть игру </Button>}

            </div>
        </div>
    );
};

export default RoomTab;