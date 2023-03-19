import React, {useContext, useEffect, useState} from 'react';
import RoomTab from "../../components/Rooms/RoomTab";
import {UserContext} from "../../context/userContext";
import RoomsAPI from "../../API/Rooms";
import {useNavigate} from "react-router-dom";
import Button from "../../components/UI/Button/Button";

const RoomsList = () => {
    const [rooms, setRooms] = useState([])
    const [userCurrentRoomId, setUserCurrentRoomId] = useState(null)

    const {user, isAuth} = useContext(UserContext)
    const navigate = useNavigate()

    useEffect(() => {
        for (const room of rooms) {
            for (const roomUser of room["users"]) {
                if (isAuth && roomUser.id === user.id && roomUser["current_room_id"]) {
                    setUserCurrentRoomId(roomUser["current_room_id"])
                }
            }
        }
    }, [rooms])

    async function addRoom() {
        const room = await RoomsAPI.createRoom(user.id)
        const roomId = room.id
        navigate(`/room/${roomId}`, {state: roomId})
    }

    async function initRooms() {
        const rooms = await RoomsAPI.getRooms()
        setRooms(rooms)
    }

    useEffect(() => {
        const room_ws = new WebSocket("ws://localhost:8000/ws/rooms/")
        room_ws.onmessage = event => {
            setRooms(JSON.parse(event.data))
        }
        initRooms()

        return () => {
            room_ws.close()
        }
    }, [])
    useEffect(() => {
        // console.log(rooms)
    }, [rooms])

    return (
        <div className={"rooms_list"}>
            {isAuth &&
                <Button className="button is-dark is-light is-outlined mx-3" onClick={addRoom}>
                    Создать комнату
                </Button>
            }
            {rooms.length !== 0
                ? rooms.map(room => {
                        // console.log(room)
                        return <RoomTab
                            roomId={room.id}
                            users={room.users}
                            isStarted={room["is_started"]}
                            key={room.id}
                            userCurrentRoomId={userCurrentRoomId}
                        />

                    }
                )
                : <h1 className="title has-text-centered">{isAuth
                    ? "Нет ни одной комнаты, создай первую!"
                    : "Еще никто не создал игру. Регистрируйся и будешь первым!"}
                </h1>
            }
        </div>
    );
};

export default RoomsList;