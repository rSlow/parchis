import React, {useState} from 'react';
import classes from "./Header.module.css";
import {Link} from "react-router-dom";

const Header = () => {
    const [isAuth, setIsAuth] = useState(false)

    return (
        <div className={classes.header}>
            <Link to={"/"} className={classes.app_name}>
                Мандавошка
            </Link>
            {isAuth
                ? <div className={classes.user_block}>
                    Профиль
                </div>
                : <div className={classes.user_block}>
                    <div className={classes.user_block__button}>
                        Войти
                    </div>
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