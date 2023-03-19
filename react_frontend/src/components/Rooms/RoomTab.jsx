import React, {useContext, useEffect, useState} from 'react';
import classes from "./RoomTab.module.css";
import {UserContext} from "../../context/userContext";
import RoomsAPI from "../../API/Rooms";
import {useNavigate} from "react-router-dom";
import Button from "../UI/Button/Button";

const RoomTab = ({roomId, isStarted, users, userCurrentRoomId}) => {

    const {user, userToken} = useContext(UserContext)
    const navigate = useNavigate()

    async function joinGame(roomId) {
        await RoomsAPI.join(user.id, roomId)
        navigate(`/room/${roomId}`, {state: roomId})
    }

    async function watchGame(room_id) {
        console.log(room_id)
    }

    return (
        <div className="box is-flex is-justify-content-space-between has-background-info-light my-3">
            ID #{roomId}
            <div className={classes.players_block}>
                Игроки: {users.length}
                <div className={"player"}>
                    {users.map(user => {
                            return <div key={user.id}>
                                #{user["id"]} {user["username"]}
                            </div>
                        }
                    )}
                </div>
            </div>
            <div className={classes.buttons_block}>

                {userToken && isStarted === false && userCurrentRoomId === null &&
                    <Button className="button is-link is-small is-outlined"
                            onClick={() => joinGame(roomId)}
                    >Присоединиться </Button>}

                {userToken && userCurrentRoomId === roomId &&
                    <Button className="button is-danger is-small is-outlined"
                            onClick={() => joinGame(roomId)}
                    > Вернуться </Button>}

                {isStarted === true && userCurrentRoomId === null &&
                    <Button className="is-success is-small mx-1"
                            onClick={() => watchGame(roomId)}
                    > Посмотреть игру </Button>}

            </div>
        </div>
    );
};

export default RoomTab;