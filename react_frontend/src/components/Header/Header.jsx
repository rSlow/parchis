import React, {useContext} from 'react';
import classes from "./Header.module.css";
import {Link} from "react-router-dom";
import {UserContext} from "../../context/userContext";

const Header = () => {
    const {user, isAuth, logout} = useContext(UserContext)

    return (
        <div className={classes.header}>
            <Link to={"/"} className={classes.app_name}>
                Мандавошка
            </Link>
            {isAuth
                ? <div className={classes.user_block}>
                    <div className={classes.user_block__button}>
                        {user.email}
                    </div>
                    <Link to={"/login/"} onClick={logout}
                          className={classes.user_block__button}
                    > Выйти </Link>

                </div>

                : <div className={classes.user_block}>
                    <Link to={"/login/"}
                          className={classes.user_block__button}
                    > Войти </Link>
                    |
                    <Link to={"/register/"}
                          className={classes.user_block__button}
                    > Регистрация </Link>
                </div>
            }
        </div>
    );
};

export default Header;