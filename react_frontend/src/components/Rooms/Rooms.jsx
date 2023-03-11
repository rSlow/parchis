import React, {useEffect, useState} from 'react';
import axios from "axios";
import RoomTab from "./RoomTab/RoomTab";

const Rooms = () => {
    const [rooms, setRooms] = useState([])

    async function setRoomsWebSocket() {
        const room_ws = new WebSocket("ws://localhost:8000/ws/rooms/")
        room_ws.onmessage = event => {
            setRooms(JSON.parse(event.data))
        }
    }

    async function addRoom() {
        await axios.post(
            "/api/rooms/",
            {}
        )
    }

    async function getRooms() {
        const response = await axios.get("/api/rooms/")
        setRooms(response.data)
    }

    useEffect(() => {
        setRoomsWebSocket()
        getRooms()
    }, [])

    return (
        <div className={"rooms_list"}>
            <button onClick={addRoom}>
                Создать комнату
            </button>
            {rooms.map(room =>
                <RoomTab
                    id={room.id}
                    key={room.id}
                    is_started={room.is_started}
                    players={room.players}
                />
            )}
        </div>
    );
};

export default Rooms;