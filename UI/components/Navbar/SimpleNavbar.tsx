'use client'

import classes from "./Navbar.module.scss";
import Link from "next/link";
import { useEffect, useState } from "react";
import { combineClasses, transformImagePaths } from "../../utils/utils";
import { LogoType, THEMES } from "../../shared/enums";
import LinkTo from "../LinkTo";
import { useTheme } from "next-themes";
import { BsFillMoonFill, BsFillSunFill, BsFillShareFill } from "react-icons/bs";
import { AiOutlineMenu, AiOutlineSearch } from "react-icons/ai";
import { iNavbar, iNavLink, iNavSocials } from "../../shared/interfaces";


const SimpleNavbar = ({ changeTheme, navSetup }: iNavbar) => {
  const { navLinks, logo } = navSetup;
  const [openDD, setOpenDD] = useState(false)
  const { theme, setTheme } = useTheme();

  return (
    <div className={combineClasses(classes.navbar__container, 'container flex items-center justify-between', "px-2")}>
      <div className="flex items-center">
        {/* <div
          className={combineClasses(classes.mobileBurgerToggle, "mr-5", openSidebar ? classes.mobileBurgerToggle__close : ' ')}
          onClick={() => toggleSideMenu()}>
          <AiOutlineMenu className="dark:text-white text-black text-2xl" />
        </div> */}
        <a href="/" className='text-[22px] font-semibold'>
          {
            logo ?
              logo.type === LogoType.IMAGE
                ?
                  <img src={theme === THEMES.DARK
                  ?
                  transformImagePaths(logo.logoLight)
                  :
                  transformImagePaths(logo.logo)} alt="WebExpe" className="cursor-pointer" width="100px" />
                :
                logo.logo : "Logo"
          }
        </a>
      </div>

      <div className="flex items-center">
        <div className='text-[14px] font-normal items-center lg:flex hidden'>
          {
            navLinks.map((each: iNavLink, i: any) => (
              each.type !== 'dropdown' && !each.newTab && each.link !== 'anchor'  ?
                <LinkTo href={each.path} key={i} passHref className='mx-2'>
                  {each.label}
                </LinkTo> :
                <a href={each.path} key={each.path + 1} rel="noopener noreferrer" className='d-block mx-2 flex-wrap'>
                  {each.label}
                </a>
            ))
          }
        </div>


        <button name="theme-switch" aria-label="theme button" className={combineClasses(classes.theme_switch, "pl-3 dark:text-white text-black")} onClick={changeTheme}>
          {
            theme && theme === 'dark' ? <BsFillSunFill className="text-2xl" /> : <BsFillMoonFill className="text-md " />
          }
        </button>
      </div>
    </div>
  );
};

export default SimpleNavbar;
