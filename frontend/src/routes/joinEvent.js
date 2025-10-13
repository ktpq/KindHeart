import Swal from "sweetalert2";
import axios from "axios";
import Cookies from "js-cookie";
import { goto } from "$app/navigation";

export const joinEvent = (event_id) => {
    console.log(event_id)
    const base_api = import.meta.env.VITE_API_URL
    const token = Cookies.get("authToken")
    Swal.fire({
        title: "Are you sure?",
        text: "คุณต้องการเข้าร่วมกิจกรรมนี้ใช่หรือไม่",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "ยืนยัน",
        cancelButtonText: "ยกเลิก",
        
        }).then(async (result) => {
        if (result.isConfirmed) {
            // ยิง api
            const response = await axios.post(`${base_api}/api/participation/`, {event: event_id}, {
                headers: { Authorization: `Token ${token}` }
            })

            console.log(response.data)
            Swal.fire({
                title: "เข้าร่วมสำเร็จ!",
                text: "สามารถดูรายละเอียดการเข้าร่วมได้ที่หน้าโปรไฟล์",
                icon: "success"
            });
        }
        });
}