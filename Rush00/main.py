work = []
date = []
work_type = []

while True:

    print("====== Smart Farm Tsk Organizer ======")
    print("1. เพิ่มงานฟาร์ม")
    print("2. แสดงรายงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")

    try:
        Text = int(input("เลือกเมนู (1-5): "))
    except ValueError:
        print("กรุณาใส่ตัวเลขเท่านั้น")
        continue

    if Text not in [1, 2, 3, 4, 5]:
        print("กรุณาเลือกเฉพาะเมนู 1-5 เท่านั้น")
        continue

    
    if Text == 1:
        work.append(input("ป้อนชื่องาน: "))
        date.append(input("ป้อนวันที่ (dd/mm/yyyy): "))
        work_type.append(input("ประเภทงาน (พืชผัก/ปศุสัตว์/อื่นๆ): "))
        print("เพิ่มงานสำดร็จ")
    elif Text == 2:
        print("รายการงานทั้งหมด:")
        if len(work) == 0:
            print("ยังไม่มีงานในรายการ")
        else:
            for i in range(len(work)):
                print(f"{i+1}. {date[i]} - {work[i]} ({work_type[i]})")
    elif Text == 3:
        print("รายการงานทั้งหมด:")
        for i in range(len(work)):
            print(f"{i+1}. {date[i]} - {work[i]} ({work_type[i]})")
        j = int(input("ลำดับของงานที่ต้องการลบ: "))
        removed = work.pop(j-1)
        del date[j-1]
        del work_type[j-1]
        print(f"ลบงาน: {removed} แล้ว")
    elif Text == 4:
        count = {}
        for item in work_type:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
        for item in count:
            print(f"- {item}: {count[item]} งาน")
    elif Text == 5:
        print("ขอบคุณที่ใช้โปรแกรม Smart Farm!")
        break