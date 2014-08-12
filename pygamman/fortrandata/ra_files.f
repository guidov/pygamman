        parameter(nx=90,ny=45,nz=33)

c
c			a program to convert the ascii data in subdirectory ./ascii
c			to random access files suitable for the routines in the
c			gamma_n library
c

        integer n(nx,ny),iocean(nx,ny)

        real along(nx),alat(ny),p(nz)
        real s(nz),t(nz),gamma(nz),a(nz)
		
		data alongw/148.0/, alatw/-44.0/

        
        print *, '  converting data ...'
       

        open(21,file='ascii/llp.dat',status='old')
        read(21,*) along,alat,p,n,iocean
        close(21)

        open(21,file='llp.fdt',status='unknown',
     &                                  form='unformatted')
        write(21) along,alat,p,n,iocean
        close(21)

        open(21,file='ascii/s.dat',status='old')
        open(22,file='ascii/t.dat',status='old')
        open(23,file='ascii/g.dat',status='old')
        open(24,file='ascii/a.dat',status='old')
        
        open(25,file='stga.fdt',access='direct',status='unknown',
     &                                   recl=528,form='unformatted')
        
        do j = 1,ny
        do i = 1,nx
        
        do k = 1,nz
          read(21,*) s(k)
          read(22,*) t(k)
          read(23,*) gamma(k)
          read(24,*) a(k)
        end do

        if(n(i,j).ne.0) then

          if(along(i).eq.alongw.and.alat(j).eq.alatw) then
                print *
                print '(3i5)', int(along(i)),int(alat(j)),n(i,j)
                do k = 1,n(i,j)
                  print '(i3,2f10.5,f12.5,f10.5,e14.5,f10.5)',  
     &                          k,s(k),t(k),p(k),gamma(k),a(k)
                end do
          end if

        end if
          
        krec = i+(j-1)*nx

        write(25,rec=krec) s,t,gamma,a

        end do
        print *, j,krec
        end do

 
        do k = 21,25
          close(k)
        end do
 
 
 
        end
