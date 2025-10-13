import { format, parseISO } from "date-fns";
export const formatDate = (date: string) => format(parseISO(date), "dd MMM yyyy");
export const formatDateTime = (date: string) => format(parseISO(date), "dd MMM yyyy, HH:mm");