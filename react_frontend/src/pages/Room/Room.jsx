import React, {useContext, useEffect, useState} from 'react';
import {useLocation, useNavigate, useNavigation, useRoutes} from "react-router-dom";
import {UserContext} from "../../context/userContext";
import RoomsAPI from "../../API/Rooms";

const Room = () => {
    const {user} = useContext(UserContext)
    const roomId = useLocation().state
    const [roomData, setRoomData] = useState({})


    useEffect(() => {
        async function initRoomData() {
            setRoomData(await RoomsAPI.getRoom(roomId))
        }

        initRoomData()
    }, [roomId])


    return (
        <div className="box has-background-light content">
            {JSON.stringify(roomData)}
        </div>
    );
};

export default Room;