pragma solidity ^0.5.7;

contract bdrs {
    struct child {
        string name;
        string time;
        string father_name;
        string mother_name;
        bool gender;
    }
    struct moredetail{
        string hospital_name;
        string blood_group;
        string doctor_name;
    }
    

//   uint256 public ChildID;

  // mapping of propertyId to Property object
//   mapping(uint256 => child) public hospital;

  
  function EnterDetails(string memory name, string memory time, string memory father_name, string memory mother_name,bool gender, string memory hospital_name, string memory blood_group, string memory doctor_name) public {
    child memory childDe = child(name,time, father_name, mother_name, gender);
    moredetail memory childDeMore = moredetail( hospital_name, blood_group, doctor_name);
    // hospital[ChildID] = childDe;
    
  }
}
