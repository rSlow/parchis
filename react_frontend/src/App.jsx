import {BrowserRouter, Route, Routes} from "react-router-dom";
import RoomsList from "./pages/RoomsList/RoomsList";
import Register from "./pages/Register/Register";
import Header from "./components/Header/Header";
import NotFound from "./pages/NotFound/NotFound";
import Login from "./pages/Login/Login";
import Room from "./pages/Room/Room";
import classes from "./App.module.css";
import About from "./pages/About/About";
import Chat from "./components/Chat/Chat";


function App() {
    return (
        <BrowserRouter>
            <Header/>
            <div className={classes.app}>
                <Routes>
                    <Route path={"/"} element={<RoomsList/>}/>
                    <Route path={"/room/:id"} element={<Room/>}/>
                    <Route path={"/login/"} element={<Login/>}/>
                    <Route path={"/register/"} element={<Register/>}/>
                    <Route path={"/about/"} element={<About/>}/>
                    <Route path="*" element={<NotFound/>}/>
                </Routes>
            </div>
            {/*<Chat/>*/}
        </BrowserRouter>

    )
}

export default App;
