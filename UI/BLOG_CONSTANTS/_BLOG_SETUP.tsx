import { LogoType, NavbarType } from "../shared/enums";
import { IAuthor, iNavSetup } from "../shared/interfaces";
import { AiFillGithub, AiOutlineTwitter, AiFillLinkedin, AiFillInstagram, AiFillFacebook } from "react-icons/ai";

/**
 * EXAMPLE AUTHOR
 * 
 export const AUTHOR_NAME: IAuthor = {
    name: "Full Name",
    designation: "Work Designation",
    bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    profilePic: "",
     social: [
        {
            icon: <AiFillGithub />,
            link: 'https://github.com/'
        },
        {
            icon: <AiFillLinkedin />,
            link: 'https://www.linkedin.com/'
        },
    ]
}
 */

export const MAYUR: IAuthor = {
    name: "Mayur Nalwala",
    designation: "Software Engineer",
    bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    profilePic: "",
    social: [
        {
            icon: <AiFillGithub />,
            link: 'https://github.com/prateekv2003/sih-1330'
        },
        {
            icon: <AiFillLinkedin />,
            link: 'https://www.linkedin.com/'
        },
    ]
}

export const RUPALI: IAuthor = {
    name: "Rupali Yadav",
    designation: "IT Analyst",
    bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    profilePic: "",
    social: [
        {
            icon: <AiFillGithub />,
            link: 'https://github.com/prateekv2003/sih-1330'
        },
        {
            icon: <AiFillLinkedin />,
            link: 'https://www.linkedin.com/in/rupali-yadav-087bb4112/'
        },
    ]
}


// This can your company name / your name
export const WEBSITE_NAME: string = 'GenMotion AI';
export const WEBSITE_URL: string = 'https://sih-text2video.vercel.app/';

/**
 * This is the main navigation setup.
 * This includes the main navbar and the side drawer.
 */
export const PRIMARY_NAV: iNavSetup = {
    type: NavbarType.CENTERED,
    // max logo image height 40px
    // you can add logo light version if using image
    // logo: {
    //     type: LogoType.IMAGE,
    //     logo: '/images/logo.png',
    //     logoLight: '/images/logo-light.png'
    // },
    logo: {
        type: LogoType.TEXT,
        logo: 'GENMOTION-AI',
    },
    // navLinks are the main navbar links that apper on top of every page
    navLinks: [
        {
            label: 'Home',
            path: '/',
            link: 'anchor'
        },
        // {
        //     label: 'Github Repo',
        //     path: 'https://github.com/prateekv2003/sih-1330',
        //     newTab: true
        // }
    ],
    // sideNavLinks are the links which appear when you open the side menu after clicking the burger menu icon.
    sideNavLinks: [
        {
            label: 'Home',
            path: '/',
            link: 'anchor'
        },
        // {
        //     label: 'Github Repo',
        //     path: 'https://github.com/prateekv2003/sih-1330',
        //     newTab: true
        // }
    ]
}