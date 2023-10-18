import dynamic from 'next/dynamic'

export const Text = dynamic(() => import('./Text/Text'))
export const Seperator = dynamic(() => import('./Seperator'))
export const LinkTo = dynamic(() => import('./LinkTo'))